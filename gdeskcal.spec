%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Eye-candy calendar for your desktop
Name:		gdeskcal
Version:	1.01
Release:	7
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.pycage.de/
Source0:	http://www.pycage.de/download/gDeskCal-%{version}.tar.gz
Source1:	gdeskcal.png
Source2:	gdeskcal.desktop
Patch0:		gdeskcal-1.0.1-fix-source-encoding.patch
BuildRequires:	desktop-file-utils
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(pygtk-2.0)
Requires:	pygtk2.0
Provides:	gDeskCal = %{EVRD}

%description
gDeskCal is a cute little eye-candy calendar for your desktop. It features
transparency with smooth alpha-blending and its appearance can be changed
completely by using skins.

%files -f %{name}.lang
%doc AUTHORS NEWS README
%{_bindir}/gdeskcal
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/

#----------------------------------------------------------------------------

%prep
%setup -q -n gDeskCal-%{version}
%patch0 -p0

%build
%configure2_5x
make
# no multi build as it's annoying the buildsys

%install
install -p -D -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/gdeskcal.png
%makeinstall_std

desktop-file-install \
	--dir ${RPM_BUILD_ROOT}%{_datadir}/applications \
	%{SOURCE2}

%find_lang %{name}

