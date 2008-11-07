%define module   Software-License
%define version    0.008
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Packages that provide templated software licenses
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Software/%{module}-%{version}.tar.gz
BuildRequires: perl(Class::ISA)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(Text::Template)
BuildRequires: perl(Data::Section)
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This packages provides templated software licenses.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/Software

