Name:		texlive-oubraces
Version:	20110325
Release:	1
Summary:	Braces over and under a formula
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oubraces
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Provides a means to interleave \overbrace and \underbrace in
the same formula.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/oubraces/oubraces.sty
%doc %{_texmfdistdir}/doc/latex/oubraces/oubraces.pdf
%doc %{_texmfdistdir}/doc/latex/oubraces/oubraces.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
