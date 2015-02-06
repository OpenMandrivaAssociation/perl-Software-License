%define upstream_name    Software-License
%define upstream_version 0.103010

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
BuildArch:  noarch

Summary:	Packages that provide templated software licenses

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Try::Tiny)
BuildRequires:	perl(Class::ISA)
BuildRequires:	perl(Data::Section)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Text::Template)

%description
This packages provides templated software licenses.

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/Software


