# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc
%define device vision
%define vendor htc
%define vendor_pretty HTC
%define device_pretty Desire Z
%define dcd_path ./
# Adjust this for your device
#%define pixel_ratio 0.89
%define pixel_ratio 0.73
# We assume most devices will
%define have_modem 1

# Community HW adaptations need this
%define community_adaptation 1

#Provides: sensord-configs

%include droid-configs-device/droid-configs.inc
