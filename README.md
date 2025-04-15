# Lab Inventory App

This is a simple yet powerful Inventory Management App designed for lab environments. It allows users to manage, track, and visualize devices with rich metadata. This app replaces traditional Excel-based tracking with a more dynamic, user-friendly solution.

## 📦 Features

- **Add, Update, and Delete Devices**
- **Search and Filter** by attributes such as Hostname, Owner, Tool, Location, VLAN, etc.
- **Boolean Flags** like Backup and Labelled for quick insights
- **Multi-MAC Support** for devices with more than one network interface
- **Commenting and Documentation** fields for context and collaboration

## 🧾 Data Model

Each device entry supports the following fields:

| Field             | Type        | Description                                |
|------------------|-------------|--------------------------------------------|
| IP Address        | `string`    | IP address of the device                   |
| Hostname          | `string`    | **Required**. Hostname of the device       |
| Owner             | `string`    | Person responsible for the device          |
| Backup            | `boolean`   | Whether the device is backed up            |
| Tool              | `string`    | Primary tool or usage associated           |
| Location          | `string`    | Physical location in the lab               |
| Asset Portfolio   | `string`    | Asset management category                  |
| Labelled          | `boolean`   | Whether the device is physically labelled  |
| MAC Address(es)   | `array`     | One or more MAC addresses                  |
| Wall Port         | `string`    | Network wall port                          |
| Switch            | `string`    | Switch name or ID                          |
| Switch Port       | `string`    | Port on the switch                         |
| VLAN              | `string`    | VLAN ID                                    |
| PVLAN             | `string`    | Private VLAN if applicable                 |
| Serial Number     | `string`    | Device serial number                       |
| Operating System  | `string`    | OS running on the device                   |
| Second Owner      | `string`    | Optional secondary owner                   |
| Comments          | `string`    | Additional notes                           |

## 🔧 Planned Features

- Charts and graphs for quick visualisation
- API for external integrations
- Scheduled backup and sync functionality

## 🚀 Getting Started

> Setup instructions coming soon.

## 🛠️ Tech Stack

- Backend: 
- Frontend: 
- Database: 
- Deployment: 


