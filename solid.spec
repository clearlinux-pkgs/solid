#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : solid
Version  : 5.111.0
Release  : 68
URL      : https://download.kde.org/stable/frameworks/5.111/solid-5.111.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.111/solid-5.111.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.111/solid-5.111.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0
Requires: solid-bin = %{version}-%{release}
Requires: solid-data = %{version}-%{release}
Requires: solid-lib = %{version}-%{release}
Requires: solid-license = %{version}-%{release}
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : flex
BuildRequires : media-player-info
BuildRequires : pkg-config
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Solid
Desktop hardware abstraction
## Introduction
%Solid is a device integration framework.  It provides a way of querying and
interacting with hardware independently of the underlying operating system.

%package bin
Summary: bin components for the solid package.
Group: Binaries
Requires: solid-data = %{version}-%{release}
Requires: solid-license = %{version}-%{release}

%description bin
bin components for the solid package.


%package data
Summary: data components for the solid package.
Group: Data

%description data
data components for the solid package.


%package dev
Summary: dev components for the solid package.
Group: Development
Requires: solid-lib = %{version}-%{release}
Requires: solid-bin = %{version}-%{release}
Requires: solid-data = %{version}-%{release}
Provides: solid-devel = %{version}-%{release}
Requires: solid = %{version}-%{release}

%description dev
dev components for the solid package.


%package lib
Summary: lib components for the solid package.
Group: Libraries
Requires: solid-data = %{version}-%{release}
Requires: solid-license = %{version}-%{release}

%description lib
lib components for the solid package.


%package license
Summary: license components for the solid package.
Group: Default

%description license
license components for the solid package.


%prep
%setup -q -n solid-5.111.0
cd %{_builddir}/solid-5.111.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698081916
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698081916
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/solid
cp %{_builddir}/solid-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/solid/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/solid-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/solid/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/solid-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/solid/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/solid-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/solid/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/solid-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/solid/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/solid-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/solid/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/solid-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/solid/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/solid-hardware5
/usr/bin/solid-hardware5

%files data
%defattr(-,root,root,-)
/usr/share/locale/ar/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/az/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/da/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/de/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/el/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/es/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/et/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/he/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/id/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/is/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/it/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/km/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/se/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/th/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/solid5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/solid5_qt.qm
/usr/share/qlogging-categories5/solid.categories
/usr/share/qlogging-categories5/solid.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Solid/Solid/Battery
/usr/include/KF5/Solid/Solid/Block
/usr/include/KF5/Solid/Solid/Camera
/usr/include/KF5/Solid/Solid/Device
/usr/include/KF5/Solid/Solid/DeviceInterface
/usr/include/KF5/Solid/Solid/DeviceNotifier
/usr/include/KF5/Solid/Solid/GenericInterface
/usr/include/KF5/Solid/Solid/NetworkShare
/usr/include/KF5/Solid/Solid/OpticalDisc
/usr/include/KF5/Solid/Solid/OpticalDrive
/usr/include/KF5/Solid/Solid/PortableMediaPlayer
/usr/include/KF5/Solid/Solid/Predicate
/usr/include/KF5/Solid/Solid/Processor
/usr/include/KF5/Solid/Solid/SolidNamespace
/usr/include/KF5/Solid/Solid/StorageAccess
/usr/include/KF5/Solid/Solid/StorageDrive
/usr/include/KF5/Solid/Solid/StorageVolume
/usr/include/KF5/Solid/solid/battery.h
/usr/include/KF5/Solid/solid/block.h
/usr/include/KF5/Solid/solid/camera.h
/usr/include/KF5/Solid/solid/device.h
/usr/include/KF5/Solid/solid/deviceinterface.h
/usr/include/KF5/Solid/solid/devicenotifier.h
/usr/include/KF5/Solid/solid/genericinterface.h
/usr/include/KF5/Solid/solid/networkshare.h
/usr/include/KF5/Solid/solid/opticaldisc.h
/usr/include/KF5/Solid/solid/opticaldrive.h
/usr/include/KF5/Solid/solid/portablemediaplayer.h
/usr/include/KF5/Solid/solid/predicate.h
/usr/include/KF5/Solid/solid/processor.h
/usr/include/KF5/Solid/solid/solid_export.h
/usr/include/KF5/Solid/solid/solidnamespace.h
/usr/include/KF5/Solid/solid/storageaccess.h
/usr/include/KF5/Solid/solid/storagedrive.h
/usr/include/KF5/Solid/solid/storagevolume.h
/usr/include/KF5/Solid/solid_version.h
/usr/lib64/cmake/KF5Solid/KF5SolidConfig.cmake
/usr/lib64/cmake/KF5Solid/KF5SolidConfigVersion.cmake
/usr/lib64/cmake/KF5Solid/KF5SolidTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Solid/KF5SolidTargets.cmake
/usr/lib64/libKF5Solid.so
/usr/lib64/qt5/mkspecs/modules/qt_Solid.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF5Solid.so.5.111.0
/V3/usr/lib64/qt5/qml/org/kde/solid/libsolidextensionplugin.so
/usr/lib64/libKF5Solid.so.5
/usr/lib64/libKF5Solid.so.5.111.0
/usr/lib64/qt5/qml/org/kde/solid/libsolidextensionplugin.so
/usr/lib64/qt5/qml/org/kde/solid/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/solid/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/solid/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/solid/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/solid/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/solid/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/solid/e458941548e0864907e654fa2e192844ae90fc32
