#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version}.0 |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name:		keysmith
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	One-Time Password client for Plasma Mobile
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/keysmith/-/archive/%{gitbranch}/keysmith-%{gitbranchd}.tar.bz2#/keysmith-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/keysmith-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	cmake(Perl)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(QXmpp)
BuildRequires:	cmake(ZXing)
BuildRequires:	qml(org.kde.prison.scanner)
BuildRequires:	cmake(KF6Prison)
BuildRequires:	pkgconfig(libsodium)
BuildRequires:	pkgconfig(openssl)

%rename plasma6-keysmith

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
One-Time Password client for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/keysmith
%{_datadir}/applications/org.kde.keysmith.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.keysmith.appdata.xml
