#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	25.08.0
%define		kframever	6.8
%define		qtver		6.6
%define		kaname		keditbookmarks
Summary:	Edit bookmarks
Name:		ka6-%{kaname}
Version:	25.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	646801214c77ad5ef08620792796bb86
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf6-ki18n-devel >= %{kframever}
BuildRequires:	kf6-kirigami-addons-devel >= 1.6.0
BuildRequires:	kf6-kirigami-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program to edit bookmarks.

%description -l pl.UTF-8
Program do edytowania zakładek.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_mandir}/zh_CN

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_desktop_database_post

%postun
/sbin/ldconfig
%update_desktop_database_postun


%files -f %{kaname}.lang
%defattr(644,root,root,755)
%doc DESIGN TODO
%attr(755,root,root) %{_bindir}/kbookmarkmerger
%attr(755,root,root) %{_bindir}/keditbookmarks
%attr(755,root,root) %{_libdir}/libkbookmarkmodel_private.so.*.*
%ghost %{_libdir}/libkbookmarkmodel_private.so.6
%{_desktopdir}/org.kde.keditbookmarks.desktop
%{_datadir}/config.kcfg/keditbookmarks.kcfg
%{_mandir}/ca/man1/kbookmarkmerger.1*
%{_mandir}/da/man1/kbookmarkmerger.1*
%{_mandir}/de/man1/kbookmarkmerger.1*
%{_mandir}/el/man1/kbookmarkmerger.1*
%{_mandir}/es/man1/kbookmarkmerger.1*
%{_mandir}/et/man1/kbookmarkmerger.1*
%{_mandir}/fr/man1/kbookmarkmerger.1*
%{_mandir}/it/man1/kbookmarkmerger.1*
%{_mandir}/man1/kbookmarkmerger.1*
%{_mandir}/nb/man1/kbookmarkmerger.1*
%{_mandir}/nl/man1/kbookmarkmerger.1*
%{_mandir}/pl/man1/kbookmarkmerger.1*
%{_mandir}/pt/man1/kbookmarkmerger.1*
%{_mandir}/pt_BR/man1/kbookmarkmerger.1*
%{_mandir}/ru/man1/kbookmarkmerger.1*
%{_mandir}/sl/man1/kbookmarkmerger.1*
%{_mandir}/sr/man1/kbookmarkmerger.1*
%{_mandir}/sr@latin/man1/kbookmarkmerger.1*
%{_mandir}/sv/man1/kbookmarkmerger.1*
%{_mandir}/tr/man1/kbookmarkmerger.1*
%{_mandir}/uk/man1/kbookmarkmerger.1*
%{_datadir}/qlogging-categories6/keditbookmarks.categories
