%include	/usr/lib/rpm/macros.php
%define		_class		Archive
%define		_subclass	Tar
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Tar file management class
Summary(pl.UTF-8):	%{_pearname} - klasa do zarządzania plikami Tar
Name:		php-pear-%{_pearname}
Version:	1.3.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3b1b2e6ddd58de6ec2925fc35b7fdfe8
URL:		http://pear.php.net/package/Archive_Tar/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of tar files in PHP. It supports
creating, listing, extracting and adding to tar files. Gzip support is
available if PHP has the zlib extension built-in or loaded.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa udostępnia obsługę plików tar w PHP. Pozwala na tworzenie,
przeglądanie zawartości, rozpakowywanie i dodawanie plików do archiwów
tar. Obsługa kompresji gzip jest dostępna, jeśli do PHP jest
zainstalowany moduł rozszerzenia zlib.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
