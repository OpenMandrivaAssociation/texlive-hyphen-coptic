%global tl_name hyphen-coptic
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Coptic hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-coptic
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-coptic.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Hyphenation patterns for Coptic in UTF-8 encoding as well as in ASCII-
based encoding for 8-bit engines. The latter can only be used with
special Coptic fonts (like CBcoptic). The patterns are considered
experimental.


%install -a
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-coptic:
coptic loadhyph-cop.tex
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/%{tl_name} <<'TL_HYPHEN_EOF'
% from hyphen-coptic:
\addlanguage{coptic}{loadhyph-cop.tex}{}{1}{1}
TL_HYPHEN_EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/%{tl_name} <<'TL_HYPHEN_EOF'
-- from hyphen-coptic:
['coptic'] = {
	loader = 'loadhyph-cop.tex',
	lefthyphenmin = 1,
	righthyphenmin = 1,
	synonyms = {  },
	patterns = 'hyph-cop.pat.txt',
},
TL_HYPHEN_EOF
