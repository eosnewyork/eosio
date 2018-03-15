/**
 *  @file
 *  @copyright defined in eos/LICENSE.txt
 */
#include <hw_poll.hpp>

using namespace eosio;

namespace hw_poll {
  void apply_create(const create& p) {

    eosio::print("Hello World: ", eosio::name(p.creator), " asked ", p.question.c_str());
  }

  /**
   *  The init() and apply() methods must have C calling convention so that the blockchain can lookup and
   *  call these methods.
   */
  extern "C" {

    /// The apply method implements the dispatch of events to this contract
    void apply( uint64_t code, uint64_t action ) {
      if (action == N(create)) {
        hw_poll::apply_create(current_action<hw_poll::create>());
      }
      else {
        eosio::print( "Hello World: ", eosio::name(code), "->", eosio::name(action), "\n" );
      }
    }

  } // extern "C"

  
}
