%global commit0 5abd767c7379aa366416d3ff32baa536327738ce
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name: conan
Version: 1.44.1
Release: 1%{?dist}

Summary: The open-source C/C++ package manager
License: MIT
URL: https://github.com/conan-io/conan
Source0: %{url}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch: requirements.patch
BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3-jwt
BuildRequires: python3-requests
BuildRequires: python3-urllib3
BuildRequires: python3-colorama
BuildRequires: python3-pyyaml
BuildRequires: python3-fasteners
BuildRequires: python3-six
BuildRequires: python3-distro
BuildRequires: python3-future
BuildRequires: python3-pygments
BuildRequires: python3-deprecation
BuildRequires: python3-tqdm
BuildRequires: python3-jinja2
BuildRequires: python3-dateutil
BuildRequires: python3-node-semver
BuildRequires: python3-patch-ng

Requires: python3-jwt
Requires: python3-six
Requires: python3-node-semver
Requires: python3-patch-ng

Requires: python3-deprecation
Requires: python3-distro
Requires: python3-jinja2
Requires: python3-pluginbase

%{?python_provide:%python_provide python3-%{name}}

%description
Conan is a package manager for C and C++ developers.

It is fully decentralized. Users can host their packages in their
servers, privately. Integrates with Artifactory and Bintray.

Portable. Works across all platforms, including Linux, OSX, Windows
(with native and first-class support, WSL, MinGW), Solaris, FreeBSD,
embedded and cross-compiling, docker, WSL.

Manage binaries. It can create, upload and download binaries for any
configuration and platform, even cross-compiling, saving lots of
time in development and continuous integration. The binary
compatibility can be configured and customized. Manage all your
artifacts in the same way on all platforms.

Integrates with any build system, including any proprietary and
custom one. Provides tested support for major build systems (CMake,
MSBuild, Makefiles, Meson, etc).

Extensible: Its python based recipes, together with extensions points
allows for great power and flexibility.

Large and active community, especially in Github and Slack. This
community also creates and maintains packages in Conan-center and
Bincrafters repositories in Bintray.

Stable. Used in production by many companies, since 1.0 there is a
commitment not to break package recipes and documented behavior.

%prep
%autosetup -n conan-%{commit0} -p1
find -type f -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%py3_build

%install
%py3_install

%files
%license LICENSE.md
%doc README.rst
%{_bindir}/%{name}*
%{python3_sitelib}/conan/
%{python3_sitelib}/conans/
%{python3_sitelib}/%{name}-*.egg-info

%changelog

* Sat Jan 15 2022 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.44.1-1
- Updated to 1.44.1

* Thu Dec 23 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.43.2-1
- Updated to 1.43.2

* Fri Nov 12 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.42.1-1
- Updated to 1.42.1

* Fri Oct 22 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.41.0-1
- Updated to 1.41.0

* Fri Oct 01 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.40.3-1
- Updated to 1.40.3

* Fri Sep 24 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.40.2-1
- Updated to 1.40.2

* Tue Sep 14 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.40.1-1
- Updated to 1.40.1

* Sat Aug 07 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.39.0-1
- Initial build
