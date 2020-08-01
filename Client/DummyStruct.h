#pragma once

#include <fstream>

// include headers that implement a archive in simple text format
#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>

namespace AI
{
	class DummyStruct
	{
	private:
		friend class boost::serialization::access;
		std::string playerName;

		template<class Archive>
		void serialize(Archive& ar, const unsigned int version)
		{
			ar& BOOST_SERIALIZATION_NVP(playerName);
		}
	public:
		DummyStruct() : playerName("bob") {};
	};
}


