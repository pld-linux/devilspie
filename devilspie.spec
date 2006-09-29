Summary:	Devil's Pie
Name:		devilspie
Version:	0.17.1
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.burtonini.com/computing/%{name}-%{version}.tar.gz
# Source0-md5:	2479a3fe9be3d7666c7f44605fa331c9
URL:		http://www.burtonini.com/blog/computers/devilspie
BuildRequires:	glib2-devel >= 2.9.1
BuildRequires:	libwnck-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A window-matching utility, inspired by Sawfish's "Matched Windows"
option and the lack of the functionality in Metacity. Metacity lacking
window matching is not a bad thing Metacity is a lean window manager,
and window matching does not have to be a window manager task.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS COPYING ChangeLog INSTALL NEWS TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}*
