%include	/usr/lib/rpm/macros.php
%define		_class		Archive
%define		_subclass	Tar
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Tar file management class
Summary(pl):	%{_pearname} - klasa do zarz�dzania plikami Tar
Name:		php-pear-%{_pearname}
Version:	0.9
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class provides handling of tar files in PHP. It supports
creating, listing, extracting and adding to tar files. Gzip support is
available if PHP has the zlib extension built-in or loaded.

%description -l pl
Ta klasa udost�pnia obs�ug� plik�w tar w PHP. Pozwala na tworzenie,
przegl�danie zawarto�ci, rozpakowywanie i dodawanie plik�w do archiw�w
tar. Obs�uga kompresji gzip jest dost�pna, je�li do PHP jest
zainstalowany modu� rozszerzenia zlib.

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
%{php_pear_dir}/%{_class}/*.php
