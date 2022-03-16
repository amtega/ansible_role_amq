# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] 2022-03-16
### Fixed

- 🐛 Fix molecule verificaton bug
- 🔥 Remove innnecesary /etc/host updating in molecule
- 🐛 Fix vars broken by code standardization in molecule
- 💬 Add ansible managed header to security settings configuration include
- 🐛 Fix artemis acceptor URL for messaging TLS. Related to ansible/roles/amtega.amq#5
- ✅ Add dhcp auto_config in molecule
- 📌 Add requirements
- Fixed tests for CentOS 8. Related to ansible/main#263

## [1.1.0] - 2022-02-08
### Changed
- Supported distros. Related to ansible/main#263
- Coding standards.
