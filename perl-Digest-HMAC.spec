%include 	/usr/lib/rpm/macros.perl
Summary:	Perl Digest-HMAC module
Summary(pl):	Modu³ Perla Digest-HMAC
Name:		perl-Digest-HMAC
Version:	1.01
Release:	1
License:	distributable
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest/Digest-HMAC-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl
Requires:	perl-Digest-MD5
Requires:	perl-Digest-SHA1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HMAC is used for message integrity checks between two parties that
share a secret key, and works in combination with some other Digest
algorithm, usually MD5 or SHA-1.  The HMAC mechanism is described in
RFC 2104.

%prep
%setup -q -n Digest-HMAC-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf README Changes rfc*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Digest/*.pm
