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
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Coptic in UTF-8 encoding as well as in ASCII-
based encoding for 8-bit engines. The latter can only be used with
special Coptic fonts (like CBcoptic). The patterns are considered
experimental.

