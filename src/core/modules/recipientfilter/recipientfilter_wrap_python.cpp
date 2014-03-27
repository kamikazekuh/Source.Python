/**
* =============================================================================
* Source Python
* Copyright (C) 2012 Source Python Development Team.  All rights reserved.
* =============================================================================
*
* This program is free software; you can redistribute it and/or modify it under
* the terms of the GNU General Public License, version 3.0, as published by the
* Free Software Foundation.
*
* This program is distributed in the hope that it will be useful, but WITHOUT
* ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
* FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
* details.
*
* You should have received a copy of the GNU General Public License along with
* this program.  If not, see <http://www.gnu.org/licenses/>.
*
* As a special exception, the Source Python Team gives you permission
* to link the code of this program (as well as its derivative works) to
* "Half-Life 2," the "Source Engine," and any Game MODs that run on software
* by the Valve Corporation.  You must obey the GNU General Public License in
* all respects for all other code used.  Additionally, the Source.Python
* Development Team grants this exception to all derivative works.
*
* Original source:
* https://developer.valvesoftware.com/wiki/Ingame_menu_for_server_plugins_(CS:S_only)
*/

//-----------------------------------------------------------------------------
// Includes
//-----------------------------------------------------------------------------
#include "modules/export_main.h"
#include "mrecipientfilter.h"
#include "modules/memory/memory_tools.h"

//-----------------------------------------------------------------------------
// Exposes the recipientfilter_c module.
//-----------------------------------------------------------------------------
void export_mrecipientfilter();

DECLARE_SP_MODULE(recipientfilter_c)
{
	export_mrecipientfilter();
}

//-----------------------------------------------------------------------------
// Expose MRecipientFilter
//-----------------------------------------------------------------------------
void export_mrecipientfilter()
{
	class_<IRecipientFilter, boost::noncopyable>("_RecipientFilter", no_init)
		.def("is_reliable",
			&IRecipientFilter::IsReliable,
			"Whether this recipient filter will be network reliable (sent in-order)"
		)

		.def("is_init_message",
			&IRecipientFilter::IsInitMessage,
			"Whether the message has been initialised?"
		)

		.def("get_recipient_count",
			&IRecipientFilter::GetRecipientCount,
			"Obtain the amount of clients in this filter"
		)

		.def("get_recipient_index",
			&IRecipientFilter::GetRecipientIndex,
			"Obtains the player index at the slot in the filter",
			args("slot")
		)

		ADD_MEM_TOOLS(IRecipientFilter, "_RecipientFilter")
	;

	// TODO: Rename class
	class_<MRecipientFilter, bases<IRecipientFilter>, boost::noncopyable >("CMRecipientFilter")
		.def("add_all_players",
			&MRecipientFilter::AddAllPlayers,
			"Adds all the players on the server to the filter"
		)

		.def("add_recipient",
			&MRecipientFilter::AddRecipient,
			"Adds the index of the player to the filter",
			args("iPlayer")
		)

		.def("remove_all_players",
			&MRecipientFilter::RemoveAllPlayers,
			"Removes all the players on the server from the filter"
		)

		.def("remove_recipient",
			&MRecipientFilter::RemoveRecipient,
			"Removes the index of the player from the filter",
			args("iPlayer")
		)

		.def("has_recipient",
			&MRecipientFilter::HasRecipient,
			"Returns true if the given index is in the recipient, false otherwise.",
			args("iPlayer")
		)

		ADD_MEM_TOOLS(MRecipientFilter, "CMRecipientFilter")
	;
}
