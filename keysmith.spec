#define snapshot 20200312
#define commit 82a4fcce5f208d749089697b045cb4bdb00bf987
#define stable %([ "`echo %{version}.0 |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		keysmith
Version:	21.08
Release:	%{?snapshot:1.%{snapshot}.}1
Summary:	One-Time Password client for Plasma Mobile
%if 0%{?snapshot:1}
Source0:	https://invent.kde.org/utilities/keysmith/-/archive/master/keysmith-%{snapshot}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Positioning)
BuildRequires:	cmake(Qt5Location)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Perl)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(QXmpp)
BuildRequires:	cmake(ZXing)
BuildRequires:	pkgconfig(libsodium)

%description
One-Time Password client for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/keysmith
%{_datadir}/applications/org.kde.keysmith.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.keysmith.appdata.xml
