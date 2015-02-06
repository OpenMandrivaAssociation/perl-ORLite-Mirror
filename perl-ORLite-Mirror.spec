%define upstream_name    ORLite-Mirror
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Extend ORLite to support remote SQLite databases
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/ORLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Remove)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Compress::Bzip2)
BuildRequires:	perl(IO::Compress::Gzip)
BuildRequires:	perl(IO::Uncompress::Bunzip2)
BuildRequires:	perl(IO::Uncompress::Gunzip)
BuildRequires:	perl(LWP::Online)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(ORLite)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
the ORLite manpage provides a readonly ORM API when it loads a readonly
SQLite database from your local system.

By combining this capability with the LWP manpage, the ORLite::Mirror
manpage goes one step better and allows you to load a SQLite database from
any arbitrary URI in readonly form as well.

As demonstrated in the synopsis above, you using the ORLite::Mirror manpage
in the same way, but provide a URL instead of a file name.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc LICENSE README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.200.0-2mdv2011.0
+ Revision: 654272
- rebuild for updated spec-helper

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2011.0
+ Revision: 499115
- update to 1.20

* Sun Jan 03 2010 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.1
+ Revision: 485905
- update to 1.18

* Sun Sep 27 2009 Jérôme Quelin <jquelin@mandriva.org> 1.170.0-1mdv2010.0
+ Revision: 450061
- update to 1.17

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.160.0-1mdv2010.0
+ Revision: 393824
- import perl-ORLite-Mirror


* Thu Jul 09 2009 cpan2dist 1.16-1mdv
- initial mdv release, generated with cpan2dist
