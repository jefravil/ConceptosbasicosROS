// Generated by gencpp from file my_custom_srv_msg_pkg/BB8CustomServiceMessage.msg
// DO NOT EDIT!


#ifndef MY_CUSTOM_SRV_MSG_PKG_MESSAGE_BB8CUSTOMSERVICEMESSAGE_H
#define MY_CUSTOM_SRV_MSG_PKG_MESSAGE_BB8CUSTOMSERVICEMESSAGE_H

#include <ros/service_traits.h>


#include <my_custom_srv_msg_pkg/BB8CustomServiceMessageRequest.h>
#include <my_custom_srv_msg_pkg/BB8CustomServiceMessageResponse.h>


namespace my_custom_srv_msg_pkg
{

struct BB8CustomServiceMessage
{

typedef BB8CustomServiceMessageRequest Request;
typedef BB8CustomServiceMessageResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct BB8CustomServiceMessage
} // namespace my_custom_srv_msg_pkg


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage > {
  static const char* value()
  {
    return "b78c0d1a37ffcec6adef7714dda05daa";
  }

  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessage&) { return value(); }
};

template<>
struct DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage > {
  static const char* value()
  {
    return "my_custom_srv_msg_pkg/BB8CustomServiceMessage";
  }

  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessage&) { return value(); }
};


// service_traits::MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest> should match
// service_traits::MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >
template<>
struct MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest>
{
  static const char* value()
  {
    return MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >::value();
  }
  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest> should match
// service_traits::DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >
template<>
struct DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest>
{
  static const char* value()
  {
    return DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >::value();
  }
  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessageRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse> should match
// service_traits::MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >
template<>
struct MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse>
{
  static const char* value()
  {
    return MD5Sum< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >::value();
  }
  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse> should match
// service_traits::DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >
template<>
struct DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse>
{
  static const char* value()
  {
    return DataType< ::my_custom_srv_msg_pkg::BB8CustomServiceMessage >::value();
  }
  static const char* value(const ::my_custom_srv_msg_pkg::BB8CustomServiceMessageResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MY_CUSTOM_SRV_MSG_PKG_MESSAGE_BB8CUSTOMSERVICEMESSAGE_H
