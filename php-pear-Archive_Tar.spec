%include	/usr/lib/rpm/macros.php
%define		_class		Archive
%define		_subclass	Tar
%define		_status		stable

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Tar file management class
Summary(pl):	%{_pearname} - klasa do zarz±dzania plikami Tar
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	474e37d367f1b96b92809baab00c0464
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/package/Archive_Tar/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of tar files in PHP. It supports
creating, listing, extracting and adding to tar files. Gzip support is
available if PHP has the zlib extension built-in or loaded.

This class has in PEAR status: %{_status}.

%description -l pl
Ta klasa udostêpnia obs³ugê plików tar w PHP. Pozwala na tworzenie,
przegl±danie zawarto¶ci, rozpakowywanie i dodawanie plików do archiwów
tar. Obs³uga kompresji gzip jest dostêpna, je¶li do PHP jest
zainstalowany modu³ rozszerzenia zlib.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_class}/*.php		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
