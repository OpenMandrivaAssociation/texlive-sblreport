%global tl_name sblreport
%global tl_revision 78595

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A LaTeX class for SBL style theses
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sblreport
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblreport.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblreport.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sblreport.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a LaTeX class for producing theses conforming to
the style required by the Society of Biblical Literature. It depends on
sblfonts for language support and biblatex-sbl for referencing.

