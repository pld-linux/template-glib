#
# Conditional build:
%bcond_without	apidocs		# API documentation
%bcond_without	static_libs	# static library

Summary:	template-glib - generate text based on a template and user defined state
Summary(pl.UTF-8):	template-glib - generowanie tekstu w oparciu o szablon i stan przekazany przez użytkownika
Name:		template-glib
Version:	3.36.3
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://download.gnome.org/sources/template-glib/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	a0031be2e974f85c97cb963b51f5988d
URL:		https://gitlab.gnome.org/GNOME/template-glib
BuildRequires:	bison
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools >= 0.18
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gobject-introspection-devel >= 0.9.5
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.20}
BuildRequires:	meson >= 0.51.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	vala
Requires:	glib2 >= 1:2.44.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Template-GLib is a library to help you generate text based on a
template and user defined state. Template-GLib does not use a language
runtime, so it is safe to use from any GObject-Introspectable
language.

Template-GLib allows you to access properties on GObjects as well as
call simple methods via GObject-Introspection.

%description -l pl.UTF-8
Template-GLib to biblioteka pomagająca generować tekst w oparciu o
szablon oraz stan przekazany przez użytkownika. Nie wykorzystuje
bibliotek językowych, więc bezpiecznie można jej używać z dowolnego
języka obsługującego GObject-Introspection.

Template-GLib pozwala na dostęp do właściwości obiektów GObject, a
także wywoływanie prostych metod poprzez GObject-Introspection.

%package devel
Summary:	Header files for the template-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki template-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.44.0
Requires:	gobject-introspection-devel >= 0.9.5

%description devel
Header files for the template-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki template-glib.

%package static
Summary:	Static template-glib library
Summary(pl.UTF-8):	Biblioteka statyczna template-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static template-glib library.

%description static -l pl.UTF-8
Biblioteka statyczna template-glib.

%package apidocs
Summary:	template-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API template-glib
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

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
BuildArch:	noarch

%description -n vala-template-glib
Template-glib API for Vala language.

%description -n vala-template-glib -l pl.UTF-8
API template-glib dla języka Vala.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dintrospection=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/libtemplate_glib-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtemplate_glib-1.0.so.0
%{_libdir}/girepository-1.0/Template-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtemplate_glib-1.0.so
%{_datadir}/gir-1.0/Template-1.0.gir
%{_includedir}/template-glib-1.0
%{_pkgconfigdir}/template-glib-1.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtemplate_glib-1.0.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/template-glib
%endif

%files -n vala-template-glib
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/template-glib-1.0.deps
%{_datadir}/vala/vapi/template-glib-1.0.vapi
