%define upstream_name    ORLite-Mirror
%define upstream_version 1.17

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Extend ORLite to support remote SQLite databases
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/ORLite/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Remove)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Compress::Bzip2)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(IO::Uncompress::Bunzip2)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(LWP::Online)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(ORLite)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc LICENSE README Changes
%{_mandir}/man3/*
%perl_vendorlib/*


