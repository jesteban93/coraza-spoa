%global debug_package %{nil}

Name:           coraza-spoa
Version:        0.1
Release:        1%{?dist}
Summary:        System daemon which brings the Coraza WAF as a backing service for HAProxy.

License:        Apache-2.0
URL:            https://github.com/corazawaf/coraza-spoa
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  golang
Requires:       libc.so.6

%description
Coraza SPOA is a system daemon which brings the Coraza Web Application Firewall (WAF) as a backing service for HAProxy

%prep
%autosetup -n %{name}-%{version}

%build
export GOPATH=%{_builddir}/go
mkdir -p $GOPATH/src/github.com/corazawaf
ln -s %{_builddir}/%{name}-%{version} $GOPATH/src/github.com/corazawaf/coraza-spoa
cd $GOPATH/src/github.com/corazawaf/coraza-spoa
go build -o %{name}

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Dec 16 2024 Jose Esteban-Infantes <j.esteban@namirial.com> - 0.1.0-1
- Initial package0
