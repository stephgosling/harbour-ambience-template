Name:       harbour-ambience-template

Summary:    Your Ambience
Version:    0.1.0
Release:    0.1
Group:      System/GUI/Other
License:    TBD
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttools-linguist
BuildRequires:  qt5-qmake
Vendor: Your Name
Packager: Your Name <your@email>

# This requirement is verboten for Harbour submission
Requires:   ambienced

%description
This is the very flowery description of your fabulous new template

%package ts-devel
Summary:   Translation source for %name
License:   TBD
Group:     System/GUI/Other

%description ts-devel
Translation source for %name

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
# Without the root directory specified it will not be removed on uninstall
%{_datadir}/ambience/%{name}
%{_datadir}/ambience/%{name}/%{name}.ambience
%{_datadir}/ambience/%{name}/sounds.index
%{_datadir}/ambience/%{name}/images/*
%{_datadir}/ambience/%{name}/sounds/*
%{_datadir}/translations/%{name}_eng_en.qm

%files ts-devel
%defattr(-,root,root,-)
%{_datadir}/translations/source/%{name}.ts


# Scripts are verboten for Harbour submission, this is only needed for
# install methods _other_ than the Store.
%post
systemctl-user restart ambienced.service

