PKG_NAME := jdk-jakarta-oro
URL := http://archive.apache.org/dist/jakarta/oro/jakarta-oro-2.0.8.tar.gz
ARCHIVES := http://repo1.maven.org/maven2/oro/oro/2.0.8/oro-2.0.8.pom %{buildroot}

include ../common/Makefile.common
