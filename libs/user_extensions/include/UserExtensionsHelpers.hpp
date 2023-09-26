#ifndef UserExtensionsHelpers_hpp
#define UserExtensionsHelpers_hpp

#include "TTAlpsEvent.hpp"
#include "ExtensionsHelpers.hpp"
#include "PhysicsObject.hpp"

inline std::shared_ptr<TTAlpsEvent> asTTAlpsEvent(const std::shared_ptr<Event> physicsObject) {
  return std::make_shared<TTAlpsEvent>(physicsObject);
}

#endif /* UserExtensionsHelpers_hpp */
