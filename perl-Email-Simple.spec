#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Email-Simple
Version  : 2.218
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Simple-2.218.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Simple-2.218.tar.gz
Summary  : 'simple parsing of RFC2822 message format and headers'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Email-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Email::Date::Format)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Email-Simple,
version 2.218:
simple parsing of RFC2822 message format and headers

%package dev
Summary: dev components for the perl-Email-Simple package.
Group: Development
Provides: perl-Email-Simple-devel = %{version}-%{release}
Requires: perl-Email-Simple = %{version}-%{release}

%description dev
dev components for the perl-Email-Simple package.


%package perl
Summary: perl components for the perl-Email-Simple package.
Group: Default
Requires: perl-Email-Simple = %{version}-%{release}

%description perl
perl components for the perl-Email-Simple package.


%prep
%setup -q -n Email-Simple-2.218
cd %{_builddir}/Email-Simple-2.218

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Email::Simple.3
/usr/share/man/man3/Email::Simple::Creator.3
/usr/share/man/man3/Email::Simple::Header.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
