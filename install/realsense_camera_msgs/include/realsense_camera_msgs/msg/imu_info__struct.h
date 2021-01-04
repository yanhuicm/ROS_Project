// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from realsense_camera_msgs:msg/IMUInfo.idl
// generated code does not contain a copyright notice

#ifndef REALSENSE_CAMERA_MSGS__MSG__IMU_INFO__STRUCT_H_
#define REALSENSE_CAMERA_MSGS__MSG__IMU_INFO__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__struct.h"

// Struct defined in msg/IMUInfo in the package realsense_camera_msgs.
typedef struct realsense_camera_msgs__msg__IMUInfo
{
  std_msgs__msg__Header header;
  double data[12];
  double noise_variances[3];
  double bias_variances[3];
} realsense_camera_msgs__msg__IMUInfo;

// Struct for a sequence of realsense_camera_msgs__msg__IMUInfo.
typedef struct realsense_camera_msgs__msg__IMUInfo__Sequence
{
  realsense_camera_msgs__msg__IMUInfo * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} realsense_camera_msgs__msg__IMUInfo__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // REALSENSE_CAMERA_MSGS__MSG__IMU_INFO__STRUCT_H_
