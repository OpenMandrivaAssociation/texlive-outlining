%global tl_name outlining
%global tl_revision 45601

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Create outlines for scientific documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/outlining
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/outlining.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Every scientifc document requires outlining before it is written. This
package adds simple macros for your LaTeX document.

