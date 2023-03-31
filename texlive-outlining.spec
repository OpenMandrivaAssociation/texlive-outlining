Name:		texlive-outlining
Version:	45601
Release:	2
Summary:	Create outlines for scientific documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/outlining
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Every scientifc document requires outlining before it is
written. This package adds simple macros for your LaTeX
document.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/outlining
%{_texmfdistdir}/tex/latex/outlining
%doc %{_texmfdistdir}/doc/latex/outlining

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
