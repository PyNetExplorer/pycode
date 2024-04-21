- name: Basic Config for Debian-based Systems
  hosts: servers
  become: true
  vars_files:
    - /home/ekaterina/ansible_quickstart/secret.yml
  vars:
    ansible_become_password: "{{ sensitive_variable }}"
    ansible_ssh_private_key_file: /home/ekaterina/.ssh/id_rsa 

  tasks:  
    - name: Update APT package lists
      apt:
        update_cache: yes

    - name: Upgrade APT packages
      apt:
        upgrade: 'yes'
        autoremove: yes

    - name: Install unattended-upgrades package
      apt:
        name: unattended-upgrades
        state: present

    - name: Ensure unattended-upgrades service is running
      service:
        name: unattended-upgrades
        enabled: yes
