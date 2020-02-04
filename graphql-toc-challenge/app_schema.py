#!/usr/bin/env python

import graphene
from bs4 import BeautifulSoup


class Quotes(graphene.ObjectType):
    quotes = graphene.List(graphene.String)

class Fortune(graphene.ObjectType):
    index = graphene.Int(description=" Index of item was in the quote")
    fortune_quote = graphene.String()

class Query(graphene.ObjectType):
    quotes = graphene.Field(Quotes, limit=graphene.Int(required=False))

    #***********query challenge starts here******#
    # Write a Graphene Field that returns a random sample of quotes from the file


    # This resolver resolves the quotes graphene field type
    def resolve_quotes(self, info, limit=None):
        infile = open("fortunes.txt", "r")
        quotes = [line.strip("\n") for line in infile]
        if limit:
            quotes = quotes[0:limit]

        return Quotes(quotes=quotes)


class HTMLTags(graphene.ObjectType):
    modified_header_tag = graphene.String()
    modified_paragraph_tag = graphene.String()


class HtmlTagsInput(graphene.Mutation):
    class Arguments:
        header_tag =graphene.List(graphene.String, required=True)
        paragraph_tag = graphene.String(required=False)

class UpdateHTMLTag(graphene.Mutation):
    class Arguments:
        tags = HtmlTagsInput()

    Output = HTMLTags()

    def mutate(self,info, header_tag,):
        pass
        # html_doc= open("FortuneTellerPage.html", "r")
        # soup = BeautifulSoup(html_doc, 'html.parser')
        # h1_elements = soup.find_all('h1')
        # return HTMLTags(modified_header_tag=header_tag, modified_paragraph_tag=paragraph_tag)

class Mutation(graphene.ObjectType):
    modify_tag = UpdateHTMLTag.Field()


schema = graphene.Schema(query=Query ,mutation=Mutation)
