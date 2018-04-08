Summary:	template-glib - generate text based on a template and user defined state
Name:		template-glib
Version:	3.28.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/template-glib/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	bae97336986704ba4f3b4921bd3cd5b3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
BuildRequires:	gtk-doc >= 1.20
BuildRequires:	meson >= 0.40.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	vala
Requires:	glib2 >= 1:2.44.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template-GLib is a library to help you generate text based on a
template and user defined state. Template-GLib does not use a language
runtime, so it is safe to use from any GObject-Introspectable
language.

Template-GLib allows you to access properties on GObjects as well as
call simple methods via GObject-Introspection. See our examples for
how to call methods.

%package devel
Summary:	Header files for the template-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki template-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0

%description devel
Header files for the template-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki template-glib.

%package apidocs
Summary:	template-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API template-glib
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Template-glib API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API template-glib.

%package -n vala-template-glib
Summary:	template-glib API for Vala language
Summary(pl.UTF-8):	API template-glib dla języka Vala
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.18.0
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-template-glib
Template-glib API for Vala language.

%description -n vala-template-glib -l pl.UTF-8
API template-glib dla języka Vala.

%prep
%setup -q

%build
%meson build \
	-Dintrospection=true \
	-Denable_gtk_doc=true

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libtemplate_glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtemplate_glib-1.0.so.0
%{_libdir}/girepository-1.0/Template-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtemplate_glib-1.0.so
%{_datadir}/gir-1.0/Template-1.0.gir
%{_includedir}/template-glib-1.0
%{_pkgconfigdir}/template-glib-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/template-glib

%files -n vala-template-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/template-glib-1.0.deps
%{_datadir}/vala/vapi/template-glib-1.0.vapi
