/**
 *  @file
 *  @copyright defined in eos/LICENSE.txt
 */
#include <eosiolib/eosio.hpp>
#include <eosiolib/db.hpp>
#include <vector>

namespace hw_poll {
  struct PACKED(create) {
    account_name creator;
    std::string question;
    //std::vector<std::string> answers;
  };
  
  struct vote {
    account_name creator;
    account_name voter;
    //std::string answer;
  };

  //using Answers = eosio::table<N(hw.poll),N(hw.poll),N(hw.poll),hw_poll::vote>;
}

