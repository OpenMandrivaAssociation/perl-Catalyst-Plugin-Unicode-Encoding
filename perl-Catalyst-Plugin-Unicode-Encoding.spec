%define upstream_name    Catalyst-Plugin-Unicode-Encoding
%define upstream_version 1.8
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.8
Release:	1

Summary:	Unicode aware Catalyst
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Unicode-Encoding-1.8.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst)
BuildRequires:	perl(Encode)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(LWP)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(Class::Data::Inheritable)
BuildArch:	noarch

%description
Catalyst plugin to wite UTF-8 web applications.
On request, it will decodes all params from encoding into a sequence of logical
characters. And it will encodes body into encoding when responding.

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
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 654269
- rebuild for updated spec-helper

* Fri Dec 17 2010 Michael Scherer <misc@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 622477
- fix missing BuildRequires
- import perl-Catalyst-Plugin-Unicode-Encoding


