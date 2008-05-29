#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	HMAC
Summary:	Digest::HMAC - keyed-hashing for message authentication
Summary(pl.UTF-8):	Digest::HMAC - haszowanie z kluczem dla uwierzytelnienia wiadomości
Name:		perl-Digest-HMAC
Version:	1.01
Release:	14
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32dc54c765100c638b5d7f7ff4c5c626
URL:		http://search.cpan.org/dist/Digest-HMAC/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	perl-Digest-SHA1 >= 1.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

%description -l pl.UTF-8
HMAC jest używany do kontroli integralności wiadomości pomiędzy dwiema
stronami dzielącymi tajny klucz, działa w połączeniu z jakimś innym
algorytmem skrótu, zazwyczaj MD5 lub SHA-1. Mechanizm HMAC jest
opisany w RFC 2104.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Digest/*.pm
%{_mandir}/man3/*
