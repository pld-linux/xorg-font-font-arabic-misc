Summary:	Arabic bitmap font
Summary(pl.UTF-8):	Font bitmapowy Arabic
Name:		xorg-font-font-arabic-misc
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-arabic-misc-%{version}.tar.xz
# Source0-md5:	e5cc79748116945cc781df5eca32e65d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Arabic bitmap font.

%description -l pl.UTF-8
Font bitmapowy Arabic (arabski).

%prep
%setup -q -n font-arabic-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/misc/arabic24.pcf.gz
