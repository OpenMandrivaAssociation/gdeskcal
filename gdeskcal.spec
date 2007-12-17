Name:           gdeskcal
Version:        1.01
Release:        %mkrel 2
Summary:        Eye-candy calendar for your desktop
Group:          Graphical desktop/GNOME
License:        GPL
URL:            http://www.pycage.de/
Source0:        http://www.pycage.de/download/gDeskCal-%{version}.tar.gz
Source1:        gdeskcal.png
Source2:        gdeskcal.desktop

BuildRequires:  desktop-file-utils, pygtk2.0-devel, perl(XML::Parser), gettext
Requires:       pygtk2.0 
Requires:       python 

BuildArch:      noarch
Provides:       gDeskCal = %{version}-%{release}

%description
gDeskCal is a cute little eye-candy calendar for your desktop.  It features
transparency with smooth alpha-blending and its appearance can be changed
completely by using skins.


%prep
%setup -q -n gDeskCal-%{version}

%build
%configure
make 
# no multi build as it's annoying the buildsys

%install
rm -rf %{buildroot}
install -p -D -m0644 %{SOURCE1} %{buildroot}/%{_datadir}/pixmaps/gdeskcal.png
make DESTDIR=%{buildroot} install

desktop-file-install 					\
  --dir ${RPM_BUILD_ROOT}%{_datadir}/applications       \
  --add-category X-MandrivaLinux                        \
  %{SOURCE2}

%find_lang %name

%post
update-desktop-database &> /dev/null ||:

%postun
update-desktop-database &> /dev/null ||:

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS NEWS README 
%{_bindir}/gdeskcal
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/
