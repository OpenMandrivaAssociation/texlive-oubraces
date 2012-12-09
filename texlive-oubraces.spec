# revision 21833
# category Package
# catalog-ctan /macros/latex/contrib/oubraces
# catalog-date 2011-03-25 11:24:40 +0100
# catalog-license noinfo
# catalog-version undef
Name:		texlive-oubraces
Version:	20110325
Release:	2
Summary:	Braces over and under a formula
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/oubraces
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/oubraces.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a means to interleave \overbrace and \underbrace in
the same formula.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110325-2
+ Revision: 754560
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110325-1
+ Revision: 719173
- texlive-oubraces
- texlive-oubraces
- texlive-oubraces
- texlive-oubraces

