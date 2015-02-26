#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Weather
%define		pnam	Underground
Summary:	Perl extension for retrieving weather information
Summary(pl.UTF-8):	Rozszerzenie Perla do odbierania informacji pogodowych
Name:		perl-Weather-Underground
Version:	3.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c86a4a807263db55ab30e44c98bcdcac
URL:		http://search.cpan.org/dist/Weather-Underground/
BuildRequires:	perl-HTML-TokeParser-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl extension for retrieving weather information from
wunderground.com.

%description -l pl.UTF-8
Rozszerzenie Perla do odbierania informacji pogodowych z
wunderground.com.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Weather
%{_mandir}/man3/*
