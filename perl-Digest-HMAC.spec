%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	HMAC
Summary:	Digest::HMAC Perl module
Summary(cs):	Modul Digest::HMAC pro Perl
Summary(da):	Perlmodul Digest::HMAC
Summary(de):	Digest::HMAC Perl Modul
Summary(es):	Módulo de Perl Digest::HMAC
Summary(fr):	Module Perl Digest::HMAC
Summary(it):	Modulo di Perl Digest::HMAC
Summary(ja):	Digest::HMAC Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Digest::HMAC ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Digest::HMAC
Summary(pl):	Modu³ Perla Digest::HMAC
Summary(pt):	Módulo de Perl Digest::HMAC
Summary(pt_BR):	Módulo Perl Digest::HMAC
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Digest::HMAC
Summary(sv):	Digest::HMAC Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Digest::HMAC
Summary(zh_CN):	Digest::HMAC Perl Ä£¿é
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
HMAC jest u¿ywany do kontroli integralno¶ci wiadomo¶ci pomiêdzy dwiema
stronami dziel±cymi tajny klucz, dzia³ w po³±czeniu z jakim¶ innym
algorytmem skrótu, zazwyczaj MD5 lub SHA-1. Mechanizm HMAC jest
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
