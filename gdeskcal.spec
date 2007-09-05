%define name gdeskcal
%define version 0.57.1
%define tarball_version 0_57_1
%define release 2mdk

Name:		%{name}
Summary:	Eye-candy calendar for GNOME desktop
Version:	%{version}
Release:	%{release}
Url:		http://www.pycage.de/software_gdeskcal.html
Source:		http://www.pycage.de/download/gDeskCal-%tarball_version.tar.gz
Patch0:		gdeskcal-0.57.1-deprecate.patch.bz2
Group:		Graphical desktop/GNOME
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	pygtk2.0 >= 2.3.90
Requires:	gnome-python-gconf

%description
gDeskCal is a cute little eye-candy calendar for your desktop.
It features transparency with smooth alpha-blending
and its appearance can be changed completely by using skins.
It can also read and display your Evolution appointments, if available.

%prep
%setup -q -n gDeskCal-%{version}
# don't use backup extension, otherwise backup files will be installed too
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_datadir/gdeskcal/
cp -a gdeskcal code data locale skins $RPM_BUILD_ROOT%_datadir/gdeskcal/
# fix bad permission
chmod +r $RPM_BUILD_ROOT%_datadir/gdeskcal/locale/lt/LC_MESSAGES/gdeskcal.mo
mkdir -p $RPM_BUILD_ROOT%_bindir/
ln -s %_datadir/gdeskcal/gdeskcal $RPM_BUILD_ROOT%_bindir/gdeskcal

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE NEWS README README.i18n README.skins
%_bindir/gdeskcal
%dir %_datadir/gdeskcal/
%_datadir/gdeskcal/gdeskcal
%_datadir/gdeskcal/code
%_datadir/gdeskcal/data
%_datadir/gdeskcal/skins
%dir %_datadir/gdeskcal/locale/
%lang(ar) %_datadir/gdeskcal/locale/ar
%lang(bg) %_datadir/gdeskcal/locale/bg
%lang(cs) %_datadir/gdeskcal/locale/cs
%lang(de) %_datadir/gdeskcal/locale/de*
%lang(el) %_datadir/gdeskcal/locale/el
%lang(es) %_datadir/gdeskcal/locale/es
%lang(fi) %_datadir/gdeskcal/locale/fi
%lang(fr) %_datadir/gdeskcal/locale/fr
%lang(he) %_datadir/gdeskcal/locale/he
%lang(hu) %_datadir/gdeskcal/locale/hu
%lang(is) %_datadir/gdeskcal/locale/is
%lang(it) %_datadir/gdeskcal/locale/it
%lang(ja) %_datadir/gdeskcal/locale/ja
%lang(ko) %_datadir/gdeskcal/locale/ko
%lang(lt) %_datadir/gdeskcal/locale/lt
%lang(nl) %_datadir/gdeskcal/locale/nl
%lang(no) %_datadir/gdeskcal/locale/no
%lang(pl) %_datadir/gdeskcal/locale/pl
%lang(ru) %_datadir/gdeskcal/locale/ru
%lang(sk) %_datadir/gdeskcal/locale/sk
%lang(sr) %_datadir/gdeskcal/locale/sr
%lang(sv) %_datadir/gdeskcal/locale/sv
%lang(tr) %_datadir/gdeskcal/locale/tr
%lang(uk) %_datadir/gdeskcal/locale/uk
%lang(zh) %_datadir/gdeskcal/locale/zh*
