; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define AppName "OpenLP"
#define AppVerName "OpenLP 2.0"
#define AppPublisher "OpenLP Developers"
#define AppURL "http://openlp.org/"
#define AppExeName "OpenLP.exe"

#define FileHandle FileOpen("..\..\dist\OpenLP\.version")
#define FileLine FileRead(FileHandle)
#define RealVersion FileLine
#expr FileClose(FileHandle)

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppID={{AA7699FA-B2D2-43F4-8A70-D497D03C9485}
AppName={#AppName}
AppVerName={#AppVerName}
AppPublisher={#AppPublisher}
AppPublisherURL={#AppURL}
AppSupportURL={#AppURL}
AppUpdatesURL={#AppURL}
DefaultDirName={pf}\{#AppName}
DefaultGroupName={#AppVerName}
AllowNoIcons=true
LicenseFile=LICENSE.txt
OutputDir=..\..\dist
OutputBaseFilename=OpenLP-{#RealVersion}-setup
Compression=lzma/Max
SolidCompression=true
SetupIconFile=OpenLP.ico
WizardImageFile=WizImageBig.bmp
WizardSmallImageFile=WizImageSmall.bmp
ChangesAssociations=true

[Languages]
Name: english; MessagesFile: compiler:Default.isl
Name: basque; MessagesFile: compiler:Languages\Basque.isl
Name: brazilianportuguese; MessagesFile: compiler:Languages\BrazilianPortuguese.isl
Name: catalan; MessagesFile: compiler:Languages\Catalan.isl
Name: czech; MessagesFile: compiler:Languages\Czech.isl
Name: danish; MessagesFile: compiler:Languages\Danish.isl
Name: dutch; MessagesFile: compiler:Languages\Dutch.isl
Name: finnish; MessagesFile: compiler:Languages\Finnish.isl
Name: french; MessagesFile: compiler:Languages\French.isl
Name: german; MessagesFile: compiler:Languages\German.isl
Name: hebrew; MessagesFile: compiler:Languages\Hebrew.isl
Name: hungarian; MessagesFile: compiler:Languages\Hungarian.isl
Name: italian; MessagesFile: compiler:Languages\Italian.isl
Name: japanese; MessagesFile: compiler:Languages\Japanese.isl
Name: norwegian; MessagesFile: compiler:Languages\Norwegian.isl
Name: polish; MessagesFile: compiler:Languages\Polish.isl
Name: portuguese; MessagesFile: compiler:Languages\Portuguese.isl
Name: russian; MessagesFile: compiler:Languages\Russian.isl
Name: slovak; MessagesFile: compiler:Languages\Slovak.isl
Name: slovenian; MessagesFile: compiler:Languages\Slovenian.isl
Name: spanish; MessagesFile: compiler:Languages\Spanish.isl

[Tasks]
Name: desktopicon; Description: {cm:CreateDesktopIcon}; GroupDescription: {cm:AdditionalIcons}
Name: quicklaunchicon; Description: {cm:CreateQuickLaunchIcon}; GroupDescription: {cm:AdditionalIcons}; OnlyBelowVersion: 0, 6.1

[Files]
Source: ..\..\dist\OpenLP\*; DestDir: {app}; Flags: ignoreversion recursesubdirs createallsubdirs
; DLL used to check if the target program is running at install time
Source: psvince.dll; flags: dontcopy
; psvince is installed in {app} folder, so it will be loaded at 
; uninstall time to check if the target program is running
Source: psvince.dll; DestDir: {app}

[Icons]
Name: {group}\{#AppName}; Filename: {app}\{#AppExeName}
Name: {group}\{#AppName} (Debug); Filename: {app}\{#AppExeName}; Parameters: -l debug
Name: {group}\{#AppName} Help; Filename: {app}\{#AppName}.chm; Check: FileExists(ExpandConstant('{app}\{#AppName}.chm'))
Name: {group}\{cm:ProgramOnTheWeb,{#AppName}}; Filename: {#AppURL}
Name: {group}\{cm:UninstallProgram,{#AppName}}; Filename: {uninstallexe}
Name: {commondesktop}\{#AppName}; Filename: {app}\{#AppExeName}; Tasks: desktopicon
Name: {userappdata}\Microsoft\Internet Explorer\Quick Launch\{#AppName}; Filename: {app}\{#AppExeName}; Tasks: quicklaunchicon

[Run]
Filename: {app}\{#AppExeName}; Description: {cm:LaunchProgram,{#AppName}}; Flags: nowait postinstall skipifsilent

[Registry]
Root: HKCR; Subkey: ".osz"; ValueType: string; ValueName: ""; ValueData: "OpenLP"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "OpenLP"; ValueType: string; ValueName: ""; ValueData: "OpenLP Service"; Flags: uninsdeletekey
Root: HKCR; Subkey: "OpenLP\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\OpenLP.exe,0"
Root: HKCR; Subkey: "OpenLP\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\OpenLP.exe"" ""%1"""

[Code]
// Function to call psvince.dll at install time
function IsModuleLoadedInstall(modulename: AnsiString ):  Boolean;
external 'IsModuleLoaded@files:psvince.dll stdcall setuponly';

// Function to call psvince.dll at uninstall time
function IsModuleLoadedUninstall(modulename: AnsiString ):  Boolean;
external 'IsModuleLoaded@{app}\psvince.dll stdcall uninstallonly' ;

function GetUninstallString(): String;
var
  sUnInstPath: String;
  sUnInstallString: String;
begin
  sUnInstPath := ExpandConstant('Software\Microsoft\Windows\CurrentVersion\Uninstall\{#emit SetupSetting("AppId")}_is1');
  sUnInstallString := '';
  if not RegQueryStringValue(HKLM, sUnInstPath, 'UninstallString', sUnInstallString) then
    RegQueryStringValue(HKCU, sUnInstPath, 'UninstallString', sUnInstallString);
  Result := sUnInstallString;
end;

function IsUpgrade(): Boolean;
begin
  Result := (GetUninstallString() <> '');
end;

// Return Values:
// 1 - uninstall string is empty
// 2 - error executing the UnInstallString
// 3 - successfully executed the UnInstallString
function UnInstallOldVersion(): Integer;
var
  sUnInstallString: String;
  iResultCode: Integer;
begin
  Result := 0;
  sUnInstallString := GetUninstallString();
  if sUnInstallString <> '' then
  begin
    sUnInstallString := RemoveQuotes(sUnInstallString);
    if Exec(sUnInstallString, '/SILENT /NORESTART /SUPPRESSMSGBOXES','', SW_HIDE, ewWaitUntilTerminated, iResultCode) then
      Result := 3
    else
      Result := 2;
  end
  else
    Result := 1;
end;

function InitializeSetup(): Boolean;
begin
  Result := true;
  while IsModuleLoadedInstall( 'OpenLP.exe' ) and Result do
  begin
    if MsgBox( 'Openlp is currently running, please close it to continue the install.',
      mbError, MB_OKCANCEL ) =  IDCANCEL then
	begin
	  Result := false;
	end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if (CurStep=ssInstall) then
  begin
    if (IsUpgrade()) then
    begin
      UnInstallOldVersion();
    end;
  end;
end;

function InitializeUninstall(): Boolean;
begin
  Result := true;
  while IsModuleLoadedUninstall( 'OpenLP.exe' ) and Result do
  begin
    if MsgBox( 'Openlp is currently running, please close it to continue the uninstall.',
      mbError, MB_OKCANCEL ) =  IDCANCEL then
	begin
	  Result := false;
	end;
  end;
end;