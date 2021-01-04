// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from realsense_camera_msgs:msg/Extrinsics.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_generator_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "realsense_camera_msgs/msg/extrinsics__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace realsense_camera_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

size_t size_function__Extrinsics__rotation(const void * untyped_member)
{
  (void)untyped_member;
  return 9;
}

const void * get_const_function__Extrinsics__rotation(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 9> *>(untyped_member);
  return &member[index];
}

void * get_function__Extrinsics__rotation(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 9> *>(untyped_member);
  return &member[index];
}

size_t size_function__Extrinsics__translation(const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * get_const_function__Extrinsics__translation(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::array<double, 3> *>(untyped_member);
  return &member[index];
}

void * get_function__Extrinsics__translation(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::array<double, 3> *>(untyped_member);
  return &member[index];
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Extrinsics_message_member_array[3] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(realsense_camera_msgs::msg::Extrinsics, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "rotation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    9,  // array size
    false,  // is upper bound
    offsetof(realsense_camera_msgs::msg::Extrinsics, rotation),  // bytes offset in struct
    nullptr,  // default value
    size_function__Extrinsics__rotation,  // size() function pointer
    get_const_function__Extrinsics__rotation,  // get_const(index) function pointer
    get_function__Extrinsics__rotation,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "translation",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(realsense_camera_msgs::msg::Extrinsics, translation),  // bytes offset in struct
    nullptr,  // default value
    size_function__Extrinsics__translation,  // size() function pointer
    get_const_function__Extrinsics__translation,  // get_const(index) function pointer
    get_function__Extrinsics__translation,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Extrinsics_message_members = {
  "realsense_camera_msgs::msg",  // message namespace
  "Extrinsics",  // message name
  3,  // number of fields
  sizeof(realsense_camera_msgs::msg::Extrinsics),
  Extrinsics_message_member_array  // message members
};

static const rosidl_message_type_support_t Extrinsics_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Extrinsics_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace realsense_camera_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<realsense_camera_msgs::msg::Extrinsics>()
{
  return &::realsense_camera_msgs::msg::rosidl_typesupport_introspection_cpp::Extrinsics_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, realsense_camera_msgs, msg, Extrinsics)() {
  return &::realsense_camera_msgs::msg::rosidl_typesupport_introspection_cpp::Extrinsics_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
