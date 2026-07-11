%global tl_name oubraces
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Braces over and under a formula
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/oubraces
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides a means to interleave \overbrace and \underbrace in the same
formula.

