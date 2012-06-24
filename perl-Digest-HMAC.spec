%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	HMAC
Summary:	Digest::HMAC Perl module
Summary(cs):	Modul Digest::HMAC pro Perl
Summary(da):	Perlmodul Digest::HMAC
Summary(de):	Digest::HMAC Perl Modul
Summary(es):	M�dulo de Perl Digest::HMAC
Summary(fr):	Module Perl Digest::HMAC
Summary(it):	Modulo di Perl Digest::HMAC
Summary(ja):	Digest::HMAC Perl �⥸�塼��
Summary(ko):	Digest::HMAC �� ����
Summary(no):	Perlmodul Digest::HMAC
Summary(pl):	Modu� Perla Digest::HMAC
Summary(pt):	M�dulo de Perl Digest::HMAC
Summary(pt_BR):	M�dulo Perl Digest::HMAC
Summary(ru):	������ ��� Perl Digest::HMAC
Summary(sv):	Digest::HMAC Perlmodul
Summary(uk):	������ ��� Perl Digest::HMAC
Summary(zh_CN):	Digest::HMAC Perl ģ��
Name:		perl-Digest-HMAC
Version:	1.01
Release:	8
License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	perl-Digest-SHA1 >= 1.00
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1. The HMAC mechanism is described in
RFC 2104.

%description -l pl
HMAC jest u�ywany do kontroli integralno�ci wiadomo�ci pomi�dzy dwiema
stronami dziel�cymi tajny klucz, dzia� w po��czeniu z jakim� innym
algorytmem skr�tu, zazwyczaj MD5 lub SHA-1. Mechanizm HMAC jest
opisany w RFC 2104.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_sitelib}/Digest/*.pm
%{_mandir}/man3/*
