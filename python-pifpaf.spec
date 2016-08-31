%global pypi_name pifpaf

%if 0%{?fedora} >= 24
%global with_python3 1
%endif

Name:           python-pifpaf
Version:        0.12.0
Release:        1%{?dist}
Summary:        Pifpaf is a suite of fixtures to manage daemons 
License:        ASL 2.0
URL:            https://github.com/jd/pifpaf
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%package -n python2-%{pypi_name}
Summary:        Pifpaf is a suite of fixtures to manage daemons
%{?python_provide:%python_provide python2-pifpaf}

BuildRequires:    python-setuptools
BuildRequires:    python2-devel

Requires:         python-cliff
Requires:         python-stevedore
Requires:         python-pbr
Requires:         python-six
Requires:         python-fixtures
Requires:         pyxattr


%description -n python2-%{pypi_name}
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage.


%if 0%{?with_python3}
%package -n python3-%{pypi_name}

Summary:          Pifpaf is a suite of fixtures to manage daemons
%{?python_provide:%python_provide python3-pifpaf}

BuildRequires:    python3-setuptools
BuildRequires:    python3-devel

Requires:         python3-cliff
Requires:         python3-stevedore
Requires:         python3-pbr
Requires:         python3-six
Requires:         python3-fixtures
Requires:         python3-pyxattr

%description -n python3-%{pypi_name}
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage. 

%endif

%description
Pifpaf is a suite of fixtures and a command-line tool that allows to start and
stop daemons for a quick throw-away usage. 

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%py2_build

%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_build
%endif

%install
%if 0%{?with_python3}
LANG=en_US.UTF-8 %py3_install
mv %{buildroot}%{_bindir}/pifpaf %{buildroot}%{_bindir}/pifpaf-%{python3_version}
ln -s ./pifpaf-%{python3_version} %{buildroot}%{_bindir}/pifpaf-3
%endif

%py2_install
mv %{buildroot}%{_bindir}/pifpaf %{buildroot}%{_bindir}/pifpaf-%{python2_version}
ln -s ./pifpaf-%{python2_version} %{buildroot}%{_bindir}/pifpaf-2

ln -s ./pifpaf-2 %{buildroot}%{_bindir}/pifpaf

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/pifpaf
%{_bindir}/pifpaf-2*
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/pifpaf-3*
%{python3_sitelib}/*
%endif


%changelog
* Fri Jul 29 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.12.0-1
- rebase to 0.12.0

* Fri Jul 29 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.6.0-2
- dropped macros
- fixed python-xattr
- fixed python3 symlink binaries

* Thu Jun 23 2016 Pradeep Kilambi <pkilambi@redhat.com> - 0.6.0-1
- initial package release
