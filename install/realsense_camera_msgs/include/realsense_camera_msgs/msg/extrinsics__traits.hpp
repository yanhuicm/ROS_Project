// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from realsense_camera_msgs:msg/Extrinsics.idl
// generated code does not contain a copyright notice

#ifndef REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__TRAITS_HPP_
#define REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__TRAITS_HPP_

#include "realsense_camera_msgs/msg/extrinsics__struct.hpp"
#include <rosidl_generator_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<realsense_camera_msgs::msg::Extrinsics>()
{
  return "realsense_camera_msgs::msg::Extrinsics";
}

template<>
struct has_fixed_size<realsense_camera_msgs::msg::Extrinsics>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<realsense_camera_msgs::msg::Extrinsics>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

}  // namespace rosidl_generator_traits

#endif  // REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__TRAITS_HPP_
